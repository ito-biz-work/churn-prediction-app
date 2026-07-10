import { Slider, Text } from "@chakra-ui/react";

interface ChargeSliderProps {
  label: string;
  value: number;
  onChange: (value: number) => void;
}

export const ChargeSlider = ({ label, value, onChange }: ChargeSliderProps) => {
  return (
    <Slider.Root 
      value={[value]} 
      min={0} 
      max={100} 
      step={0.1} 
      onValueChange={(e) => onChange(e.value[0])}
      mb={4}
      colorPalette="cyan"
    >
      <Slider.Label display="flex" justifyContent="space-between" mb={1}>
        <Text fontWeight="bold" as="span">{label}</Text>
        <Text fontWeight="bold" as="span">{value.toFixed(2)} ドル</Text>
      </Slider.Label>
      <Slider.Control>
        <Slider.Track>
          <Slider.Range />
        </Slider.Track>
        <Slider.Thumb index={0} />
      </Slider.Control>
    </Slider.Root>
  );
};