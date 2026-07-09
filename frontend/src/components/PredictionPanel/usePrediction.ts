import { useState, useCallback } from "react";
import { API_VERSION } from "@/config/constants";
import { type Customer } from "@/types/customer";

export interface PredictionResult {
  probability: number;
}

export const usePrediction = () => {
  const [prediction, setPrediction] = useState<PredictionResult | null>(null);
  const [loading, setLoading] = useState(false);

  const runSimulation = useCallback(async (customer: Customer, params: {
    dayCharge: number;
    eveCharge: number;
    nightCharge: number;
  }) => {
    setLoading(true);
    try {
      const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
      const response = await fetch(`${API_BASE_URL}/api/${API_VERSION}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...customer,
          totalDayCharge: params.dayCharge,
          totalEveCharge: params.eveCharge,
          totalNightCharge: params.nightCharge,
        }),
      });
      
      const data: PredictionResult = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error("予測計算エラー:", error);
    } finally {
      setLoading(false);
    }
  }, []);

  // 顧客切り替え時に予測結果をリセット
  const resetPrediction = useCallback(() => setPrediction(null), []);

  return { prediction, loading, runSimulation, resetPrediction };
};