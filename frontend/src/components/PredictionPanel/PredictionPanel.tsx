import { Box, Text, Spinner, Flex, Heading } from "@chakra-ui/react";
import { ProbabilityCard } from "./ProbabilityCard";
import { CustomerDetails } from "./CustomerDetails";
import { usePrediction } from "./usePrediction";
import { type Customer } from "@/types/customer";

// ラッパーの用意
const PanelContainer = ({ children }: { children: React.ReactNode }) => (
  <Box
    flex="1"
    p={6}
    bg="bg.panel"
    shadow="md"
    borderWidth="1px"
    borderRadius="lg"
  >
    {children}
  </Box>
);

export default function PredictionPanel({ customer }: { customer: Customer | null }) {
  const { prediction, loading, runSimulation } = usePrediction();
  // 予測結果がある場合はそれを使用
  const displayProbability = prediction?.probability ?? customer?.churnProbability ?? 0;

  return (
    <PanelContainer>
      {!customer ? (
        <Text color="fg.subtle" textAlign="center">顧客を選択すると、ここに詳細が表示されます。</Text>
      ) : (
        <>
          <Flex align="center" justify="space-between" mb={3} mr={3}>
            <Heading size="lg">退会確率シミュレータ</Heading>
            <Text fontSize="sm" color="fg.subtle">対象顧客: {customer.customerName} 様</Text>
          </Flex>

          <Box position="relative">
            {loading && (
              <Box 
                position="absolute" 
                top={0} left={0} right={0} bottom={0} 
                bg="whiteAlpha.700" 
                display="flex" alignItems="center" justifyContent="center"
                zIndex={1}
              >
                <Spinner size="lg" />
              </Box>
            )}
            <ProbabilityCard probability={displayProbability} />
          </Box>

          <CustomerDetails 
            key={customer.id}
            customer={customer} 
            onSimulate={runSimulation} 
          />
        </>
      )}
    </PanelContainer>
  );
}