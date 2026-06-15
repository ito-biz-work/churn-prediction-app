import { Box, Text } from "@chakra-ui/react";

export const ProbabilityCard = ({ probability }: { probability: number }) => {
  const getProbabilityColor = (prob: number) => {
    if (prob >= 0.8) return "red.solid";
    if (prob >= 0.4) return "yellow.focusRing";
    return "green.solid";
  };

  return (
    <Box p={3} bg="bg.subtle" borderRadius="md" borderWidth="1px" mb={3}>
      <Text
        fontSize="4xl"
        fontWeight="extrabold"
        color={getProbabilityColor(probability)}
      >
        {(probability * 100).toFixed(0)}%
      </Text>
    </Box>
  );
};
