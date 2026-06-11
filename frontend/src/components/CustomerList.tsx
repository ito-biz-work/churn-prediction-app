import { useState, useEffect } from "react";
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
  customerName: string;
  customerCode: string;
};

interface CustomerListProps {
  onSelect: (customer: Customer) => void;
}

const PAGE_SIZE = 5;

export default function CustomerList({ onSelect }: CustomerListProps) {
  const [totalCount, setTotalCount] = useState(0);
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(true);

  // 顧客情報取得
  // ページ更新時のみ実行
  useEffect(() => {
    const fetchCustomers = async () => {
      setLoading(true);
      try {
        const skip = (page - 1) * PAGE_SIZE;
        const response = await fetch(
          `http://localhost:8000/api/v1/customers?skip=${skip}&limit=${PAGE_SIZE}`,
        );
        const data = await response.json();
        setTotalCount(data.totalCount);
        setCustomers(data.items);
      } catch (error) {
        console.log("データ取得エラー:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchCustomers();
  }, [page]);

  if (loading) return <Box>読み込み中...</Box>;

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
        count={totalCount}
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
