import { Box, Heading, Text, DataList } from "@chakra-ui/react";

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
      <Box p={8} bg="bg.panel" shadow="md" borderWidth="1px" borderColor="border" borderRadius="lg" textAlign="center" >
        <Text color="fg.subtle" fontWeight="medium">
          顧客を選択すると、ここに予測結果が表示されます。
        </Text>
      </Box>
    );
  }

  return (
    <Box p={6} bg="bg.panel" shadow="md" borderWidth="1px" borderColor="border" borderRadius="lg">
      <Heading size="lg" mb={6}>予測結果詳細</Heading>
      
      {/* 退会確率 */}
      <Box p={6} bg="bg.subtle" borderRadius="md" borderWidth="1px" borderColor="border" mb={6}>
        <Text fontSize="sm" fontWeight="semibold" color="fg.muted" textTransform="uppercase" letterSpacing="wide" mb={1}>
          退会確率
        </Text>
        <Text fontSize="4xl" fontWeight="extrabold" color="red.solid">85%</Text>
      </Box>

      {/* 顧客属性情報 */}
      <Box borderWidth="1px" borderColor="border" borderRadius="md" overflow="hidden">
        <Box bg="bg.subtle" p={3} borderBottomWidth="1px" borderColor="border">
          <Text fontWeight="semibold" fontSize="sm" color="fg.muted" letterSpacing="wide">
            顧客属性情報
          </Text>
        </Box>
        <Box p={4}>
          <DataList.Root orientation="horizontal">
            <DataList.Item>
              <DataList.ItemLabel>氏名</DataList.ItemLabel>
              <DataList.ItemValue>田中 太郎</DataList.ItemValue>
            </DataList.Item>
            <DataList.Item>
              <DataList.ItemLabel>居住州</DataList.ItemLabel>
              <DataList.ItemValue>NJ</DataList.ItemValue>
            </DataList.Item>
            <DataList.Item>
              <DataList.ItemLabel>エリアコード</DataList.ItemLabel>
              <DataList.ItemValue>area_code_415</DataList.ItemValue>
            </DataList.Item>
            <DataList.Item>
              <DataList.ItemLabel>契約期間</DataList.ItemLabel>
              <DataList.ItemValue>55ヶ月</DataList.ItemValue>
            </DataList.Item>
          </DataList.Root>
        </Box>
      </Box>
    </Box>
  );
}