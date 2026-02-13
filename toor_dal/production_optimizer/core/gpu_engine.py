"""
GPU Engine Module
Provides utilities for CUDA device management and tensor generation.
"""
import torch


def get_device():
    """
    Returns the CUDA device or raises an error if unavailable.

    Returns:
        torch.device: The CUDA device object (cuda:0).

    Raises:
        RuntimeError: If CUDA is not available.
    """
    if not torch.cuda.is_available():
        raise RuntimeError(
            "CRITICAL ERROR: CUDA GPU not detected. Optimization requires GPU acceleration.")

    device = torch.device("cuda:0")
    return device


def set_precision(use_double=True):
    """
    Sets default tensor precision.

    Args:
        use_double (bool): If True, sets default dtype to float64 (Double).
                           If False, sets to float32 (Float).
    """
    if use_double:
        torch.set_default_dtype(torch.float64)
    else:
        torch.set_default_dtype(torch.float32)


def get_uniform_tensor(low, high, size, device):
    """
    Generates a uniform distribution tensor on GPU.

    Args:
        low (float): Lower bound.
        high (float): Upper bound.
        size (int/tuple): Size of the tensor.
        device (torch.device): Device to create tensor on.

    Returns:
        torch.Tensor: Random tensor drawn from U(low, high).
    """
    return (torch.rand(size, device=device) * (high - low)) + low
