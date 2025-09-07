[] Create S3 bucket + upload upscaled CIFAR-10.

[] IAM role/user with least-priv perms.

[] Implement rek_detect_labels.py + retries + logging.

[] Build label mapping (label_map.json).

[] Run smoke test on 100 images; inspect results.

[] Full batch run; log per-image JSONL + latencies.

[] Compute metrics (acc/precision/recall/F1 macro/weighted).

[] Plot threshold–F1 and latency histograms.

[] Fill pricing.yml from current AWS page; compute costs.

[] (Optional) Train & benchmark Custom Labels.

[] Write docs/aws_pipeline.md with methods, configs, and results.
