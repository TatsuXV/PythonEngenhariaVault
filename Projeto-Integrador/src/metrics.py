from dataclasses import dataclass
from typing import List, Dict
import logging

@dataclass
class TaskMetrics:
    name: str
    start_time: float
    end_time: float
    status: str
    attempts: int

class PipelineSummary:
    """Gera um relatório detalhado da execução da DAG."""
    def __init__(self, dag_name: str):
        self.dag_name = dag_name
        self.metrics: List[TaskMetrics] = []

    def add_metric(self, metric: TaskMetrics):
        self.metrics.append(metric)

    def generate_report(self) -> str:
        report = [
            f"\n{'='*50}",
            f"AURORA ENGINE - EXECUTION SUMMARY",
            f"DAG: {self.dag_name}",
            f"{'='*50}",
            f"{'Task Name':<25} | {'Status':<10} | {'Duration':<10} | {'Retries':<8}",
            f"{'-'*50}"
        ]

        total_duration = 0
        for m in self.metrics:
            duration = m.end_time - m.start_time
            total_duration += duration
            report.append(f"{m.name:<25} | {m.status:<10} | {duration:>8.2f}s | {m.attempts:>8}")

        report.append(f"{'-'*50}")
        report.append(f"Total Pipeline Runtime: {total_duration:.2f}s")
        report.append(f"{'='*50}\n")

        return "\n".join(report)
