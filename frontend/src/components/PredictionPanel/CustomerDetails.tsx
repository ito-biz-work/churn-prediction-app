import { useState, useEffect } from "react";
import { Box, Flex, Text } from "@chakra-ui/react";
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

  // ステートを監視してデバウンス処理
  useEffect(() => {
    // 初期状態（すべてのスライダーが初期値のまま）なら何もせず終了
    if (
      dayCharge === customer.totalDayCharge &&
      eveCharge === customer.totalEveCharge &&
      nightCharge === customer.totalNightCharge
    ) return;
    
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
          <Text fontWeight="semibold" fontSize="sm" color="fg.muted">通話料金</Text>
        </Flex>
      </Box>
      <Box p={4}>
        {/* スライダー */}
        <ChargeSlider label="昼" value={dayCharge} onChange={setDayCharge} />
        <ChargeSlider label="夕" value={eveCharge} onChange={setEveCharge} />
        <ChargeSlider label="夜" value={nightCharge} onChange={setNightCharge} />
      </Box>
    </Box>
  );
};
