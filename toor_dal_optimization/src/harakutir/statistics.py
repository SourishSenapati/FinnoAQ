"""
Statistical analysis engine for Harakutir Toor Dal study.
Implements Welch's t-test, Mann-Whitney U, Cohen's d effect sizes,
Holm-Bonferroni correction, confidence intervals, and data-gated validation.
"""

import numpy as np
import scipy.stats as stats
from typing import Dict, Any, List, Tuple, Optional

def compute_descriptive_stats(values: List[float], alpha: float = 0.05) -> Dict[str, Any]:
    """Compute descriptive statistics with sample size and 95% CI."""
    arr = np.array(values, dtype=np.float64)
    arr = arr[~np.isnan(arr)]
    n = len(arr)
    if n == 0:
        return {"n": 0, "status": "no_data"}
    
    mean = float(np.mean(arr))
    std = float(np.std(arr, ddof=1)) if n > 1 else 0.0
    median = float(np.median(arr))
    q25, q75 = float(np.percentile(arr, 25)), float(np.percentile(arr, 75))
    iqr = q75 - q25
    
    # 95% Confidence Interval for the mean
    if n > 1 and std > 0:
        se = std / np.sqrt(n)
        t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
        ci_lower = mean - t_crit * se
        ci_upper = mean + t_crit * se
    else:
        ci_lower = mean
        ci_upper = mean
        
    return {
        "n": n,
        "mean": round(mean, 4),
        "std": round(std, 4),
        "median": round(median, 4),
        "q25": round(q25, 4),
        "q75": round(q75, 4),
        "iqr": round(iqr, 4),
        "ci_95_lower": round(ci_lower, 4),
        "ci_95_upper": round(ci_upper, 4),
        "min": round(float(np.min(arr)), 4),
        "max": round(float(np.max(arr)), 4)
    }

def compute_comparative_stats(
    group_a: List[float],
    group_b: List[float],
    name_a: str = "Tanzanian",
    name_b: str = "Indian Benchmark",
    alpha: float = 0.05
) -> Dict[str, Any]:
    """
    Perform rigorous two-sample comparative analysis:
    - Welch's t-test (unequal variance)
    - Mann-Whitney U test (non-parametric)
    - Cohen's d effect size with 95% CI
    """
    a = np.array(group_a, dtype=np.float64)
    b = np.array(group_b, dtype=np.float64)
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]
    
    n_a, n_b = len(a), len(b)
    if n_a < 2 or n_b < 2:
        return {
            "status": "insufficient_sample_size",
            "n_a": n_a,
            "n_b": n_b,
            "message": "At least 2 observations per group required for comparative hypothesis testing."
        }
        
    mean_a, mean_b = float(np.mean(a)), float(np.mean(b))
    var_a, var_b = float(np.var(a, ddof=1)), float(np.var(b, ddof=1))
    
    # Welch's t-test
    t_stat, p_val_welch = stats.ttest_ind(a, b, equal_var=False)
    
    # Satterthwaite degrees of freedom
    denom = ((var_a / n_a) ** 2) / (n_a - 1) + ((var_b / n_b) ** 2) / (n_b - 1)
    df_welch = ((var_a / n_a + var_b / n_b) ** 2) / denom if denom > 0 else (n_a + n_b - 2)
    
    # Mann-Whitney U test
    try:
        u_stat, p_val_mw = stats.mannwhitneyu(a, b, alternative="two-sided")
    except Exception:
        u_stat, p_val_mw = np.nan, np.nan
        
    # Cohen's d effect size (pooled standard deviation)
    s_pooled = np.sqrt(((n_a - 1) * var_a + (n_b - 1) * var_b) / (n_a + n_b - 2))
    diff = mean_a - mean_b
    cohens_d = diff / s_pooled if s_pooled > 0 else 0.0
    
    # Approximate 95% CI for Cohen's d
    se_d = np.sqrt((n_a + n_b) / (n_a * n_b) + (cohens_d ** 2) / (2 * (n_a + n_b)))
    z_crit = 1.96
    d_ci_lower = cohens_d - z_crit * se_d
    d_ci_upper = cohens_d + z_crit * se_d
    
    return {
        "status": "success",
        "group_a": name_a,
        "group_b": name_b,
        "n_a": n_a,
        "n_b": n_b,
        "mean_a": round(mean_a, 4),
        "mean_b": round(mean_b, 4),
        "absolute_difference": round(diff, 4),
        "welch_t_statistic": round(float(t_stat), 4),
        "degrees_of_freedom": round(float(df_welch), 2),
        "p_value_welch": float(p_val_welch),
        "mann_whitney_u": float(u_stat),
        "p_value_mann_whitney": float(p_val_mw),
        "cohens_d": round(float(cohens_d), 4),
        "cohens_d_95_ci": [round(float(d_ci_lower), 4), round(float(d_ci_upper), 4)],
        "significant_at_alpha": bool(p_val_welch < alpha)
    }

def apply_holm_bonferroni(p_values: List[float], alpha: float = 0.05) -> List[Dict[str, Any]]:
    """
    Adjust p-values for family-wise error rate control using Holm-Bonferroni method.
    """
    m = len(p_values)
    if m == 0:
        return []
    
    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
    adjusted = [None] * m
    
    running_max = 0.0
    for rank, (orig_idx, p) in enumerate(indexed):
        adj_p = p * (m - rank)
        adj_p = min(1.0, max(adj_p, running_max))
        running_max = adj_p
        adjusted[orig_idx] = {
            "original_p": float(p),
            "adjusted_p": float(adj_p),
            "significant": bool(adj_p < alpha)
        }
    return adjusted
