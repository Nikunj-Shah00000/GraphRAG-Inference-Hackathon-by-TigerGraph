"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

import { Card } from "@/components/ui/card";

const data = [
  {
    name: "LLM Only",
    wasted: 7000,
    useful: 4200,
  },
  {
    name: "Basic RAG",
    wasted: 2200,
    useful: 2600,
  },
  {
    name: "GraphRAG",
    wasted: 400,
    useful: 1500,
  },
];

export default function TokenHeatmap() {
  return (
    <Card className="p-6 rounded-2xl shadow-xl">
      <h2 className="text-2xl font-bold mb-6">
        Token Efficiency Heatmap
      </h2>

      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="name" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="useful" stackId="a" />

          <Bar dataKey="wasted" stackId="a" />
        </BarChart>
      </ResponsiveContainer>

      <div className="mt-4 text-sm text-gray-500">
        Lower wasted token usage indicates better retrieval efficiency.
      </div>
    </Card>
  );
}