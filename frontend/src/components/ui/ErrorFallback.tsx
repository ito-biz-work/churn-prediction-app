import { Box, Heading, Text, Button, VStack } from "@chakra-ui/react";
import type { FallbackProps } from "react-error-boundary";

export const ErrorFallback = ({ error, resetErrorBoundary }: FallbackProps) => {
  // errorがErrorオブジェクトのインスタンスかどうか
  const errorMessage = error instanceof Error ? error.message : String(error);

  return (
    <Box
      minH="100vh"
      display="flex"
      alignItems="center"
      justifyContent="center"
      px={6}
      bg="bg.subtle"
    >
      <VStack gap={6} maxW="lg" textAlign="center">
        <Heading size="lg" color="fg.error">
          予期せぬエラーが発生しました
        </Heading>

        <Text color="fg.muted">
          ページの表示中に問題が発生しました。
          <br />
          お手数ですが、もう一度お試しください。
        </Text>

        {import.meta.env.DEV && (
          <Box
            w="100%"
            p={4}
            bg="bg.error"
            color="fg.error"
            borderWidth="1px"
            borderColor="border.error"
            borderRadius="md"
            textAlign="left"
            fontSize="sm"
            fontFamily="mono"
          >
            {errorMessage}
          </Box>
        )}

        <Button colorPalette="red" size="lg" onClick={resetErrorBoundary}>
          もう一度試す
        </Button>
      </VStack>
    </Box>
  );
};
