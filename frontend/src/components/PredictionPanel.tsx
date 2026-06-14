import { Box, Heading, Text, DataList, Flex } from "@chakra-ui/react";
import { useState, useEffect } from "react";
import { type Customer } from "./CustomerList";

interface PredictionOutput {
  probability: number;
}

export default function PredictionPanel({
  customer,
}: {
  customer: Customer | null;
}) {
  const [prediction, setPrediction] = useState<PredictionOutput | null>(null);
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
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(customer),
        });
        const data = await response.json();
        setPrediction(data);
      } catch (error) {
        console.log("データ取得エラー:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPrediction();
  }, [customer]);

  if (loading) return <Box>読み込み中...</Box>;

  // 顧客が選択されていない場合の表示
  if (!customer || !prediction) {
    return (
      <Box
        flex="1"
        p={6}
        bg="bg.panel"
        shadow="md"
        borderWidth="1px"
        borderColor="border"
        borderRadius="lg"
        textAlign="center"
      >
        <Text color="fg.subtle" fontWeight="medium">
          顧客を選択すると、ここに予測結果が表示されます。
        </Text>
      </Box>
    );
  }

  const customerFields = [
    { label: "契約期間", value: `${customer.accountLength} ヶ月` },
    { label: "昼間の通話時間", value: `${customer.totalDayMinutes} 分` },
    { label: "昼間の通話料金", value: `${customer.totalDayCharge} ドル` },
    { label: "夕方の通話時間", value: `${customer.totalEveMinutes} 分` },
    { label: "夕方の通話料金", value: `${customer.totalEveCharge} ドル` },
    { label: "夜間の通話時間", value: `${customer.totalNightMinutes} 分` },
    { label: "夜間の通話料金", value: `${customer.totalNightCharge} ドル` },
  ];

  const getProbabilityColor = (prob: number) => {
    if (prob >= 0.8) return "red.solid"; // 高リスク：赤
    if (prob >= 0.4) return "yellow.focusRing"; // 中リスク：黄
    return "green.solid"; // 低リスク：緑
  };

  return (
    <Box
      flex="1"
      p={6}
      bg="bg.panel"
      shadow="md"
      borderWidth="1px"
      borderColor="border"
      borderRadius="lg"
    >
      <Flex align="center" justify="space-between">
        <Heading size="lg" mb={3}>
          退会確率
        </Heading>
        <Text fontSize="sm" mb={3} mr={3} color="fg.muted" opacity={0.8}>
          対象顧客: {customer.customerName} 様
        </Text>
      </Flex>

      {/* 退会確率 */}
      <Box
        p={3}
        bg="bg.subtle"
        borderRadius="md"
        borderWidth="1px"
        borderColor="border"
        mb={3}
      >
        <Text
          fontSize="4xl"
          fontWeight="extrabold"
          color={getProbabilityColor(prediction.probability)}
        >
          {(prediction.probability * 100).toFixed(0)}%
        </Text>
      </Box>

      {/* 重要項目 */}
      <Box
        borderWidth="1px"
        borderColor="border"
        borderRadius="md"
        overflow="hidden"
      >
        <Box bg="bg.muted" p={3} borderBottomWidth="1px" borderColor="border">
          <Flex align="center" justify="space-between">
            <Text
              fontWeight="semibold"
              fontSize="sm"
              color="fg.muted"
              letterSpacing="wide"
            >
              重要項目
            </Text>
            <Text fontSize="xs" color="fg.muted" opacity={0.8}>
              ※上位7項目
            </Text>
          </Flex>
        </Box>
        <Box p={4}>
          <DataList.Root orientation="horizontal">
            {customerFields.map((item) => (
              <DataList.Item key={item.label}>
                <DataList.ItemLabel>{item.label}</DataList.ItemLabel>
                <DataList.ItemValue>{item.value}</DataList.ItemValue>
              </DataList.Item>
            ))}
          </DataList.Root>
        </Box>
      </Box>
    </Box>
  );
}
