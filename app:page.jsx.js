"use client";

import GraphVisualization from "@/components/GraphVisualization";
import TokenHeatmap from "@/components/TokenHeatmap";
import StrategyBadge from "@/components/StrategyBadge";

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-7xl mx-auto space-y-8">

        <div>
          <h1 className="text-5xl font-bold">
            GraphReduce AI
          </h1>

          <p className="text-gray-400 mt-3">
            GraphRAG Inference Optimization Platform
          </p>
        </div>

        <StrategyBadge strategy="graph" />

        <GraphVisualization />

        <TokenHeatmap />

      </div>
    </main>
  );
}