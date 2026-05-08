export default function StrategyBadge({ strategy }) {
  const styles = {
    vector: "bg-blue-500",
    graph: "bg-green-500",
    hybrid: "bg-purple-500",
  };

  return (
    <div
      className={`px-4 py-2 rounded-full text-white text-sm font-semibold ${styles[strategy]}`}
    >
      {strategy.toUpperCase()} RETRIEVAL
    </div>
  );
}