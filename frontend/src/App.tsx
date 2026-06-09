import { useState } from 'react';
import { Box, Flex, Heading, Text } from "@chakra-ui/react"; // 必要なコンポーネントをインポート
import CustomerList, { type Customer } from './components/CustomerList';
import PredictionPanel from './components/PredictionPanel';

function App() {
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(null);

  return (
    <Flex direction="column" minH="100vh" bg="gray.50">
      {/* ヘッダー */}
      <Box as="header" bg="blue.900" p={4} shadow="md">
        <Heading size="md" color="white" letterSpacing="wide">
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
      <Box as="footer" bg="gray.200" borderTop="1px" borderColor="gray.300" p={4} textAlign="center">
        <Text fontSize="sm" color="gray.600">
          © 2026 Customer Insights System
        </Text>
      </Box>
    </Flex>
  );
}

export default App;