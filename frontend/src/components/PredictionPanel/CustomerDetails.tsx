import { useState, useEffect, useRef } from "react";
import { Box, Flex, Text, DataList } from "@chakra-ui/react";
import { type Customer } from "@/types/customer";
import { ChargeSlider } from "./ChargeSlider";

interface CustomerDetailsProps {
  customer: Customer;
  onSimulate: (
    customer: Customer,
    params: { dayCharge: number; eveCharge: number; nightCharge: number }
  ) => Promise<void>;
}

export const CustomerDetails = ({ customer, onSimulate }: CustomerDetailsProps) => {
  // customerの値を初期値としてセット
  const [dayCharge, setDayCharge] = useState(customer.totalDayCharge);
  const [eveCharge, setEveCharge] = useState(customer.totalEveCharge);
  const [nightCharge, setNightCharge] = useState(customer.totalNightCharge);

  const timeFields = [
    { label: "昼間", value: `${customer.totalDayMinutes} 分` },
    { label: "夕方", value: `${customer.totalEveMinutes} 分` },
    { label: "夜間", value: `${customer.totalNightMinutes} 分` },
  ];

  const isInitialMount = useRef(true);

  // ステートを監視してデバウンス処理
  useEffect(() => {
    // 初回レンダリング時はAPIを叩かないようにする
    if (isInitialMount.current) {
      isInitialMount.current = false;
      return;
    }
    
    // シミュレーションを実行する関数
    const timerId = setTimeout(() => {
      onSimulate(customer, {
        dayCharge,
        eveCharge,
        nightCharge,
      });
    }, 500);

    // 0.5秒以内にステートが更新されたら、前のタイマーを破棄
    return () => clearTimeout(timerId);
  }, [dayCharge, eveCharge, nightCharge, customer, onSimulate]);

  return (
    <Box
      borderWidth="1px"
      borderColor="border"
      borderRadius="md"
      overflow="hidden"
    >
      <Box bg="bg.muted" p={3} borderBottomWidth="1px" borderColor="border">
        <Flex align="center" justify="space-between">
          <Text fontWeight="semibold" fontSize="sm" color="fg.muted">確率シミュレータ</Text>
        </Flex>
      </Box>
      <Box p={4}>
        <Text fontWeight="semibold" fontSize="md" pb={3}>通話料金</Text>

        {/* スライダー */}
        <ChargeSlider label="昼間" value={dayCharge} onChange={setDayCharge} />
        <ChargeSlider label="夕方" value={eveCharge} onChange={setEveCharge} />
        <ChargeSlider label="夜間" value={nightCharge} onChange={setNightCharge} />
      </Box>
      <Box p={4}>
        <Text fontWeight="semibold" fontSize="md" pb={3}>通話時間</Text>
        <DataList.Root orientation="horizontal">
          {timeFields.map((item) => (
            <DataList.Item key={item.label}>
              <DataList.ItemLabel>{item.label}</DataList.ItemLabel>
              <DataList.ItemValue>{item.value}</DataList.ItemValue>
            </DataList.Item>
          ))}
        </DataList.Root>
      </Box>
    </Box>
  );
};
