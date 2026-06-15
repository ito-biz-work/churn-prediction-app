import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import { type Customer } from "@/types/customer";

const PAGE_SIZE = 5;

export const useCustomers = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [totalCount, setTotalCount] = useState(0);
  const [loading, setLoading] = useState(true);

  // URLのpageパラメータを数値として取得
  const page = parseInt(searchParams.get("page") || "1", 10);

  useEffect(() => {
    const fetchCustomers = async () => {
      setLoading(true);
      try {
        const skip = (page - 1) * PAGE_SIZE;
        const response = await fetch(
          `http://localhost:8000/api/v1/customers?skip=${skip}&limit=${PAGE_SIZE}`
        );
        const data = await response.json();
        setTotalCount(data.totalCount);
        setCustomers(data.items);
      } catch (error) {
        console.error("データ取得エラー:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchCustomers();
  }, [page, setCustomers, setLoading, setTotalCount]);

  const handlePageChange = (newPage: number) => {
    setSearchParams({ page: newPage.toString() });
  };

  return {
    customers,
    loading,
    totalCount,
    page,
    PAGE_SIZE,
    handlePageChange,
  };
};