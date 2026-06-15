import { Box, Flex, Text, DataList } from "@chakra-ui/react";
import { type Customer } from "@/types/customer";

export const CustomerDetails = ({ customer }: { customer: Customer }) => {
  const fields = [
    { label: "契約期間", value: `${customer.accountLength} ヶ月` },
    { label: "昼間の通話時間", value: `${customer.totalDayMinutes} 分` },
    { label: "昼間の通話料金", value: `${customer.totalDayCharge} ドル` },
    { label: "夕方の通話時間", value: `${customer.totalEveMinutes} 分` },
    { label: "夕方の通話料金", value: `${customer.totalEveCharge} ドル` },
    { label: "夜間の通話時間", value: `${customer.totalNightMinutes} 分` },
    { label: "夜間の通話料金", value: `${customer.totalNightCharge} ドル` },
  ];

  return (
    <Box
      borderWidth="1px"
      borderColor="border"
      borderRadius="md"
      overflow="hidden"
    >
      <Box bg="bg.muted" p={3} borderBottomWidth="1px" borderColor="border">
        <Flex align="center" justify="space-between">
          <Text fontWeight="semibold" fontSize="sm" color="fg.muted">
            重要項目
          </Text>
          <Text fontSize="xs" color="fg.subtle">
            ※上位7項目
          </Text>
        </Flex>
      </Box>
      <Box p={4}>
        <DataList.Root orientation="horizontal">
          {fields.map((item) => (
            <DataList.Item key={item.label}>
              <DataList.ItemLabel>{item.label}</DataList.ItemLabel>
              <DataList.ItemValue>{item.value}</DataList.ItemValue>
            </DataList.Item>
          ))}
        </DataList.Root>
      </Box>
    </Box>
  );
};
