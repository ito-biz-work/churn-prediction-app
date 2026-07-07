import { Table, Button } from "@chakra-ui/react";
import { type Customer } from "@/types/customer";

interface CustomerTableProps {
  customers: Customer[];
  onSelect: (customer: Customer) => void;
}

export const CustomerTable = ({ customers, onSelect }: CustomerTableProps) => {
  return (
    <Table.Root size="md" variant="outline">
      <Table.Header>
        <Table.Row>
          <Table.ColumnHeader color="fg.muted">ID</Table.ColumnHeader>
          <Table.ColumnHeader color="fg.muted">氏名</Table.ColumnHeader>
          <Table.ColumnHeader color="fg.muted">顧客コード</Table.ColumnHeader>
          <Table.ColumnHeader />
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {customers.map((customer) => (
          <Table.Row key={customer.id}>
            <Table.Cell>{customer.id}</Table.Cell>
            <Table.Cell>{customer.customerName}</Table.Cell>
            <Table.Cell>{customer.customerCode}</Table.Cell>
            <Table.Cell textAlign="end">
              <Button
                colorPalette="cyan"
                size="sm"
                shadow="sm"
                onClick={() => onSelect(customer)}
              >
                詳細
              </Button>
            </Table.Cell>
          </Table.Row>
        ))}
      </Table.Body>
    </Table.Root>
  );
};
