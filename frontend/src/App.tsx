import { useState } from "react";
import { Box, Flex, Heading, Text } from "@chakra-ui/react";
import CustomerList, { type Customer } from "./components/CustomerList";
import PredictionPanel from "./components/PredictionPanel";

function App() {
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(
    null,
  );

  return (
    <Flex direction="column" minH="100vh" bg="bg.subtle">
      {/* ヘッダー */}
      <Box as="header" bg="cyan.fg" p={4} shadow="md">
        <Heading size="md" color="cyan.contrast" letterSpacing="wide">
          顧客分析ダッシュボード
        </Heading>
      </Box>

      {/* メインコンテンツ */}
      <Flex as="main" flex="1" p={6} gap={6}>
        <Box w="50%">
          <CustomerList onSelect={setSelectedCustomer} />
        </Box>
        <Box w="50%">
          <PredictionPanel customer={selectedCustomer} />
        </Box>
      </Flex>

      {/* フッター */}
      <Box
        as="footer"
        bg="bg.muted"
        borderTop="1px"
        borderColor="border.emphasized"
        p={4}
        textAlign="center"
      >
        <Text fontSize="sm" color="fg.muted">
          © 2026 Customer Insights System
        </Text>
      </Box>
    </Flex>
  );
}

export default App;
