import { useState, useEffect } from "react";
import { Box, Flex, Text } from "@chakra-ui/react";
import { type Customer } from "@/types/customer";
import { MinutesSlider } from "./MinutesSlider";

interface SimulatorFormProps {
  customer: Customer;
  onSimulate: (
    customer: Customer,
    params: { dayMinutes: number; eveMinutes: number; nightMinutes: number }
  ) => Promise<void>;
}

export const SimulatorForm = ({ customer, onSimulate }: SimulatorFormProps) => {
  // customerの値を初期値としてセット
  const [dayMinutes, setDayMinutes] = useState(customer.totalDayMinutes);
  const [eveMinutes, setEveMinutes] = useState(customer.totalEveMinutes);
  const [nightMinutes, setNightMinutes] = useState(customer.totalNightMinutes);

  // ステートを監視してデバウンス処理
  useEffect(() => {
    // 初期状態（すべてのスライダーが初期値のまま）なら何もせず終了
    if (
      dayMinutes === customer.totalDayMinutes &&
      eveMinutes === customer.totalEveMinutes &&
      nightMinutes === customer.totalNightMinutes
    ) return;
    
    // シミュレーションを実行する関数
    const timerId = setTimeout(() => {
      onSimulate(customer, {
        dayMinutes,
        eveMinutes,
        nightMinutes,
      });
    }, 500);

    // 0.5秒以内にステートが更新されたら、前のタイマーを破棄
    return () => clearTimeout(timerId);
  }, [dayMinutes, eveMinutes, nightMinutes, customer, onSimulate]);

  return (
    <Box
      borderWidth="1px"
      borderColor="border"
      borderRadius="md"
      overflow="hidden"
    >
      <Box bg="bg.muted" p={3} borderBottomWidth="1px" borderColor="border">
        <Flex align="center" justify="space-between">
          <Text fontWeight="semibold" fontSize="sm" color="fg.muted">通話時間</Text>
        </Flex>
      </Box>
      <Box p={4}>
        {/* スライダー */}
        <MinutesSlider label="昼" value={dayMinutes} onChange={setDayMinutes} />
        <MinutesSlider label="夕" value={eveMinutes} onChange={setEveMinutes} />
        <MinutesSlider label="夜" value={nightMinutes} onChange={setNightMinutes} />
      </Box>
    </Box>
  );
};
