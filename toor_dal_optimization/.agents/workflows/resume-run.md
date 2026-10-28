# Resume Client Organization Run

Resume the existing Client Organization local supervisor from the latest verified checkpoint. Do not reset or overwrite state. Validate manifest and checkpoint hashes, reconcile interrupted tasks, check run lock/resources, run quick integrity tests, then resume only the next safe idempotent task. Preserve real/synthetic data separation. Update status and exact resume command. Do not claim completion unless the audit/release gates pass.
