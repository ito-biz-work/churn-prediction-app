import { Box, Heading, Button, Table } from "@chakra-ui/react";

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

interface CustomerListProps {
  onSelect: (customer: Customer) => void;
}

export default function CustomerList({ onSelect }: CustomerListProps) {
  return (
    <Box bg="white" p={6} shadow="md" borderWidth="1px" borderColor="gray.200" borderRadius="lg">
      <Heading size="lg" mb={4}>顧客一覧</Heading>
      
      <Box borderWidth="1px" borderColor="gray.200" borderRadius="md" overflow="hidden">
        <Table.Root size="md" variant="outline">
          <Table.Header>
            <Table.Row>
              <Table.ColumnHeader>ID</Table.ColumnHeader>
              <Table.ColumnHeader>氏名</Table.ColumnHeader>
              <Table.ColumnHeader>顧客コード</Table.ColumnHeader>
              <Table.ColumnHeader />
            </Table.Row>
          </Table.Header>

          <Table.Body>
            {customers.map((customer) => (
              <Table.Row key={customer.id}>
                <Table.Cell>{customer.id}</Table.Cell>
                <Table.Cell>{customer.name}</Table.Cell>
                <Table.Cell>{customer.code}</Table.Cell>
                <Table.Cell textAlign="end">
                  <Button 
                    colorPalette="blue" 
                    size="sm" 
                    shadow="sm"
                    onClick={() => onSelect(customer)}
                  >
                    実行
                  </Button>
                </Table.Cell>
              </Table.Row>
            ))}
          </Table.Body>
        </Table.Root>
      </Box>
    </Box>
  );
}