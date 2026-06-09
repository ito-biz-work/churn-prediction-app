import { Box, Heading, Button, Grid, GridItem } from "@chakra-ui/react";

export type Customer = {
  id: number;
  name: string;
  code: string;
};

// 仮データ
const customers: Customer[] = [
  { id: 1, name: "田中 太郎", code: "CUST001" },
  { id: 2, name: "佐藤 花子", code: "CUST002" },
  { id: 3, name: "鈴木 一郎", code: "CUST003" },
];


// 型を定義
interface CustomerListProps {
  onSelect: (customer: Customer) => void;
}

export default function CustomerList({ onSelect }: CustomerListProps) {
  return (
    <Box bg="white" p={6} shadow="md" borderWidth="1px" borderColor="gray.200" borderRadius="lg">
      <Heading size="lg" mb={4}>顧客一覧</Heading>
      
      <Box borderWidth="1px" borderColor="gray.200" borderRadius="md" overflow="hidden">
        {/* ヘッダー */}
        <Grid templateColumns="repeat(4, 1fr)" gap={2} p={3} bg="gray.50" borderBottomWidth="1px" borderColor="gray.200" fontWeight="semibold" fontSize="sm" color="gray.600" textTransform="uppercase" letterSpacing="wider">
          <GridItem>ID</GridItem>
          <GridItem>氏名</GridItem>
          <GridItem>顧客コード</GridItem>
          <GridItem />
        </Grid>

        {/* 顧客リスト */}
        {customers.map((customer) => (
          <Grid 
            key={customer.id} 
            templateColumns="repeat(4, 1fr)" 
            gap={2} 
            p={3} 
            borderBottomWidth="1px" 
            borderColor="gray.100" 
            alignItems="center"
            _last={{ borderBottomWidth: 0 }}
            fontSize="md" 
            color="gray.900"
          >
            <GridItem>{customer.id}</GridItem>
            <GridItem>{customer.name}</GridItem>
            <GridItem>{customer.code}</GridItem>
            <GridItem>
              <Button 
                colorPalette="blue" 
                size="sm" 
                shadow="sm"
                onClick={() => onSelect(customer)}
              >
                実行
              </Button>
            </GridItem>
          </Grid>
        ))}
      </Box>
    </Box>
  );
}