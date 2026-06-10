import { useState } from "react";
import {
  Box,
  Heading,
  Button,
  Table,
  Pagination,
  IconButton,
  ButtonGroup,
} from "@chakra-ui/react";
import { LuChevronLeft, LuChevronRight } from "react-icons/lu";

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
  { id: 4, name: "高橋 誠", code: "CUST004" },
  { id: 5, name: "伊藤 由美", code: "CUST005" },
];

interface CustomerListProps {
  onSelect: (customer: Customer) => void;
}

const PAGE_SIZE = 2;

export default function CustomerList({ onSelect }: CustomerListProps) {
  const [page, setPage] = useState(1);

  // ページに応じたデータ切り出し
  const paginatedCustomers = customers.slice(
    (page - 1) * PAGE_SIZE,
    page * PAGE_SIZE,
  );

  return (
    <Box
      display="flex"
      flexDirection="column"
      minH="50vh"
      bg="bg.panel"
      p={6}
      shadow="md"
      borderWidth="1px"
      borderColor="border"
      borderRadius="lg"
    >
      <Heading size="lg" mb={4}>
        顧客一覧
      </Heading>

      {/* Table */}
      <Box flex="1" overflow="auto" mb={4}>
        <Table.Root size="md" variant="outline">
          <Table.Header>
            <Table.Row>
              <Table.ColumnHeader color="fg.muted">ID</Table.ColumnHeader>
              <Table.ColumnHeader color="fg.muted">氏名</Table.ColumnHeader>
              <Table.ColumnHeader color="fg.muted">
                顧客コード
              </Table.ColumnHeader>
              <Table.ColumnHeader />
            </Table.Row>
          </Table.Header>
          <Table.Body>
            {paginatedCustomers.map((customer) => (
              <Table.Row key={customer.id}>
                <Table.Cell>{customer.id}</Table.Cell>
                <Table.Cell>{customer.name}</Table.Cell>
                <Table.Cell>{customer.code}</Table.Cell>
                <Table.Cell textAlign="end">
                  <Button
                    colorPalette="cyan"
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

      {/* Pagination */}
      <Pagination.Root
        count={customers.length}
        pageSize={PAGE_SIZE}
        page={page}
        onPageChange={(e) => setPage(e.page)}
      >
        <ButtonGroup variant="outline" size="sm" justifyContent="center">
          <Pagination.PrevTrigger asChild>
            <IconButton>
              <LuChevronLeft />
            </IconButton>
          </Pagination.PrevTrigger>

          <Pagination.Items
            render={(p) => (
              <IconButton variant={p.value === page ? "surface" : "ghost"}>
                {p.value}
              </IconButton>
            )}
          />

          <Pagination.NextTrigger asChild>
            <IconButton>
              <LuChevronRight />
            </IconButton>
          </Pagination.NextTrigger>
        </ButtonGroup>
      </Pagination.Root>
    </Box>
  );
}
