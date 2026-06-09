import { Box, Heading, Text, SimpleGrid } from "@chakra-ui/react";

// 顧客データの型を定義
interface Customer {
  id: number;
  name: string;
  code: string;
}

interface PredictionPanelProps {
  customer: Customer | null;
}

export default function PredictionPanel({ customer }: PredictionPanelProps) {
  // 顧客が選択されていない場合の表示
  if (!customer) {
    return (
      <Box p={8} bg="white" shadow="md" borderWidth="1px" borderColor="gray.200" borderRadius="lg" color="gray.500" textAlign="center">
        顧客を選択すると、ここに予測結果が表示されます。
      </Box>
    );
  }

  return (
    <Box p={6} bg="white" shadow="md" borderWidth="1px" borderColor="gray.200" borderRadius="lg">
      <Heading size="lg" mb={6}>予測結果詳細</Heading>
      
      {/* 退会確率 */}
      <Box p={6} bg="gray.50" borderRadius="md" borderWidth="1px" borderColor="gray.200" mb={6}>
        <Text fontSize="sm" fontWeight="semibold" color="gray.600" textTransform="uppercase" letterSpacing="wide" mb={1}>
          退会確率
        </Text>
        <Text fontSize="4xl" fontWeight="extrabold" color="red.600">85%</Text>
      </Box>

      {/* 顧客属性情報 */}
      <Box borderWidth="1px" borderColor="gray.200" borderRadius="md" overflow="hidden">
        <Box bg="gray.50" p={3} fontWeight="semibold" fontSize="sm" color="gray.600" borderBottomWidth="1px" borderColor="gray.200" textTransform="uppercase" letterSpacing="wide">
          顧客属性情報
        </Box>
        <Box p={4}>
          <SimpleGrid columns={2} gap={4}>
            <Text fontWeight="bold" color="gray.500" whiteSpace="nowrap">氏名:</Text>
            <Text>田中 太郎</Text>

            <Text fontWeight="bold" color="gray.500" whiteSpace="nowrap">居住州:</Text>
            <Text>NJ</Text>

            <Text fontWeight="bold" color="gray.500" whiteSpace="nowrap">エリアコード:</Text>
            <Text>area_code_415</Text>

            <Text fontWeight="bold" color="gray.500" whiteSpace="nowrap">契約期間:</Text>
            <Text>55ヶ月</Text>
          </SimpleGrid>
        </Box>
      </Box>
    </Box>
  );
}