import { useState } from "react";
import { Box, Flex, Heading, Text } from "@chakra-ui/react";
import CustomerList from "./components/CustomerList/CustomerList";
import PredictionPanel from "./components/PredictionPanel/PredictionPanel";
import { type Customer } from "./types/customer";

function App() {
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(
    null,
  );

  return (
    <Flex direction="column" minH="100vh" bg="bg.subtle">
      {/* ヘッダー */}
      <Box as="header" bg="cyan.fg" p={3} shadow="md">
        <Heading size="md" color="cyan.contrast" letterSpacing="wide">
          退会予測ダッシュボード
        </Heading>
      </Box>

      {/* メインコンテンツ */}
      <Flex as="main" flex="1" p={5} gap={5} align="stretch">
        <Box flex="2" display="flex" flexDirection="column">
          <CustomerList onSelect={setSelectedCustomer} />
        </Box>
        <Box flex="1" display="flex" flexDirection="column">
          <PredictionPanel
            key={selectedCustomer?.id ?? "empty"}
            customer={selectedCustomer}
          />
        </Box>
      </Flex>

      {/* フッター */}
      <Box
        as="footer"
        bg="bg.muted"
        borderTop="1px"
        borderColor="border.emphasized"
        p={3}
        textAlign="center"
      >
        <Text fontSize="sm" color="fg.muted">
          © 2026 Customer Churn Prediction Dashboard
        </Text>
      </Box>
    </Flex>
  );
}

export default App;
