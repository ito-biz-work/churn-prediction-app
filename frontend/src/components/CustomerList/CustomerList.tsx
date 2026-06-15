import { Box, Heading, Spinner } from "@chakra-ui/react";
import { useCustomers } from "./useCustomers";
import { CustomerTable } from "./CustomerTable";
import { PaginationControls } from "./PaginationControls";
import { type Customer } from "@/types/customer";

interface CustomerListProps {
  onSelect: (customer: Customer) => void;
}

export default function CustomerList({ onSelect }: CustomerListProps) {
  const { customers, loading, totalCount, page, PAGE_SIZE, handlePageChange } =
    useCustomers();

  return (
    <Box
      p={6}
      flex="1"
      display="flex"
      flexDirection="column"
      minH="50vh"
      bg="bg.panel"
      shadow="md"
      borderWidth="1px"
      borderColor="border"
      borderRadius="lg"
    >
      {/* Header */}
      <Heading size="lg" mb={4}>
        顧客一覧
      </Heading>

      {loading ? (
        // ローディング中の表示
        <Box
          flex="1"
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <Spinner size="lg" />
        </Box>
      ) : (
        // 一覧表示
        <>
          {/* Table */}
          <Box flex="1" overflow="auto" mb={4}>
            <CustomerTable customers={customers} onSelect={onSelect} />
          </Box>

          {/* Pagination */}
          <PaginationControls
            totalCount={totalCount}
            pageSize={PAGE_SIZE}
            page={page}
            onPageChange={handlePageChange}
          />
        </>
      )}
    </Box>
  );
}
