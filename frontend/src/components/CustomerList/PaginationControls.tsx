import { Pagination, IconButton, ButtonGroup } from "@chakra-ui/react";
import { LuChevronLeft, LuChevronRight } from "react-icons/lu";

interface PaginationControlsProps {
  totalCount: number;
  pageSize: number;
  page: number;
  onPageChange: (page: number) => void;
}

export const PaginationControls = ({
  totalCount,
  pageSize,
  page,
  onPageChange,
}: PaginationControlsProps) => {
  return (
    <Pagination.Root
      count={totalCount}
      pageSize={pageSize}
      page={page}
      onPageChange={(e) => onPageChange(e.page)}
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
  );
};
