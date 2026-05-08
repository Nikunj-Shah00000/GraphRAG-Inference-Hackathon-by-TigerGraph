"use client";

import dynamic from "next/dynamic";
import { Card } from "@/components/ui/card";

const ForceGraph2D = dynamic(
  () => import("react-force-graph").then((mod) => mod.ForceGraph2D),
  { ssr: false }
);

export default function GraphVisualization() {
  const data = {
    nodes: [
      { id: "Transformer", group: 1 },
      { id: "Attention", group: 1 },
      { id: "Efficiency", group: 2 },
      { id: "Inference", group: 2 },
      { id: "Token Reduction", group: 3 },
    ],
    links: [
      { source: "Transformer", target: "Attention" },
      { source: "Attention", target: "Efficiency" },
      { source: "Efficiency", target: "Inference" },
      { source: "Inference", target: "Token Reduction" },
    ],
  };

  return (
    <Card className="p-4 rounded-2xl shadow-xl">
      <h2 className="text-2xl font-bold mb-4">
        GraphRAG Relationship Visualization
      </h2>

      <div className="h-[500px]">
        <ForceGraph2D
          graphData={data}
          nodeLabel="id"
          linkDirectionalArrowLength={4}
          linkDirectionalArrowRelPos={1}
          nodeAutoColorBy="group"
          cooldownTicks={100}
        />
      </div>
    </Card>
  );
}