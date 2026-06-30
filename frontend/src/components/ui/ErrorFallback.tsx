import { Box, Heading, Code, Button, VStack } from '@chakra-ui/react';
import type { FallbackProps } from 'react-error-boundary';

export const ErrorFallback = ({ error, resetErrorBoundary }: FallbackProps) => {
  // errorがErrorオブジェクトのインスタンスかどうか
  const errorMessage = error instanceof Error ? error.message : String(error);

  return (
    <Box 
      p={6}
      flex="1"
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      minH="50vh"
      bg="bg.panel"
      shadow="md"
      borderWidth="1px"
      borderColor="border"
      borderRadius="lg"
    >
      <VStack spaceY={4} maxW="xl" width="100%" textAlign="center">
        <Heading size="lg" color="red.fg">
          申し訳ありません。予期せぬエラーが発生しました。
        </Heading>
        
        {/* エラー内容 */}
        <Code 
          p={4} 
          borderRadius="md" 
          variant="subtle"
          bg="bg.error"
          color="fg.error"
          width="100%"
          whiteSpace="pre-wrap"
          textAlign="left"
        >
          {errorMessage}
        </Code>
        
        <Button 
          colorPalette="red" 
          onClick={resetErrorBoundary}
          size="md"
        >
          アプリを再起動する
        </Button>
      </VStack>
    </Box>
  );
};