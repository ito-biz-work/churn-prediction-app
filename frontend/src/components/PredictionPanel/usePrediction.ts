import { useState, useEffect } from "react";
import { type Customer } from "@/types/customer";

export const usePrediction = (customer: Customer | null) => {
  const [prediction, setPrediction] = useState<{ probability: number } | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!customer) {
      queueMicrotask(() => setPrediction(null));
      return;
    }

    const fetchPrediction = async () => {
      setLoading(true);
      try {
        const response = await fetch("http://localhost:8000/api/v1/predict", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(customer),
        });
        const data = await response.json();
        setPrediction(data);
      } catch (error) {
        console.error("データ取得エラー:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPrediction();
  }, [customer]);

  return { prediction, loading };
};