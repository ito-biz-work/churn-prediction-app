import { Box, Heading, Text, DataList, Flex } from "@chakra-ui/react";
import { useState, useEffect } from "react";
import { type Customer } from "./CustomerList";

// 型
interface CustomerDetail {
  accountLength: number;
  totalDayMinutes: number;
  totalDayCharge: number;
  totalEveMinutes: number;
  totalEveCharge: number;
  totalNightMinutes: number;
  totalNightCharge: number;
}

interface PredictionFields {
  probability: number;
}

interface PredictionOutput {
  customer: CustomerDetail;
  probability: PredictionFields["probability"];
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
        const response = await fetch(
          `http://localhost:8000/api/v1/predict?customer_id=${customer.id}`,
        );
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
        p={8}
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
    { label: "契約期間", value: `${prediction.customer.accountLength} ヶ月` },
    {
      label: "昼間の通話時間",
      value: `${prediction.customer.totalDayMinutes} 分`,
    },
    {
      label: "昼間の通話料金",
      value: `${prediction.customer.totalDayCharge} ドル`,
    },
    {
      label: "夕方の通話時間",
      value: `${prediction.customer.totalEveMinutes} 分`,
    },
    {
      label: "夕方の通話料金",
      value: `${prediction.customer.totalEveCharge} ドル`,
    },
    {
      label: "夜間の通話時間",
      value: `${prediction.customer.totalNightMinutes} 分`,
    },
    {
      label: "夜間の通話料金",
      value: `${prediction.customer.totalNightCharge} ドル`,
    },
  ];

  const getProbabilityColor = (prob: number) => {
    if (prob >= 0.8) return "red.solid"; // 高リスク：赤
    if (prob >= 0.4) return "yellow.focusRing"; // 中リスク：黄
    return "green.solid"; // 低リスク：緑
  };

  return (
    <Box
      p={6}
      bg="bg.panel"
      shadow="md"
      borderWidth="1px"
      borderColor="border"
      borderRadius="lg"
    >
      <Heading size="lg" mb={6}>
        予測結果
      </Heading>

      {/* 退会確率 */}
      <Box
        p={6}
        bg="bg.subtle"
        borderRadius="md"
        borderWidth="1px"
        borderColor="border"
        mb={6}
      >
        <Text
          fontSize="sm"
          fontWeight="semibold"
          color="fg.muted"
          letterSpacing="wide"
          mb={1}
        >
          退会確率
        </Text>
        <Text
          fontSize="4xl"
          fontWeight="extrabold"
          color={getProbabilityColor(prediction.probability)}
        >
          {(prediction.probability * 100).toFixed(0)}%
        </Text>
      </Box>

      {/* 退会予測の重要項目 */}
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
              退会予測の重要項目
            </Text>
            <Text fontSize="xs" color="fg.muted" opacity={0.8}>
              ※重要度上位7項目
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
