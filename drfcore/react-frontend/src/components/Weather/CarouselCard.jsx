import React, { useState } from "react";
import { useTheme } from "@mui/material/styles";
import MobileStepper from "@mui/material/MobileStepper";
import Button from "@mui/material/Button";
import KeyboardArrowLeft from "@mui/icons-material/KeyboardArrowLeft";
import KeyboardArrowRight from "@mui/icons-material/KeyboardArrowRight";
import SecondaryCard from "./SecondaryCard";
import { Container } from "@mui/material";
import clocks from "../common/data/clocks.json";
const CarouselCard = ({ onCardCityChange }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const startIndex = currentIndex;
  const endIndex = startIndex + 3;
  const theme = useTheme();
  const [activeStep, setActiveStep] = React.useState(0);
  const maxSteps = clocks.length / 3;
  const totalCards = clocks.length;

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
    setCurrentIndex((prevIndex) => (prevIndex + 3) % totalCards);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
    setCurrentIndex((prevIndex) => (prevIndex - 3 + totalCards) % totalCards);
  };

  const handleCityChange = (city) => {
    onCardCityChange(city);
  };
  return (
    <>
      <Container sx={{ display: "flex" }}>
        <SecondaryCard
          partOfArray={clocks.slice(startIndex, endIndex)}
          onCityChange={handleCityChange}
        />
      </Container>
      <MobileStepper
        variant="text"
        steps={maxSteps}
        position="static"
        activeStep={activeStep}
        sx={{
          maxWidth: 400,
          flexGrow: 1,
          ml: "10em",
        }}
        nextButton={
          <Button
            size="small"
            onClick={handleNext}
            disabled={activeStep === maxSteps - 1}
          >
            Next
            {theme.direction === "rtl" ? (
              <KeyboardArrowLeft />
            ) : (
              <KeyboardArrowRight />
            )}
          </Button>
        }
        backButton={
          <Button size="small" onClick={handleBack} disabled={activeStep === 0}>
            {theme.direction === "rtl" ? (
              <KeyboardArrowRight />
            ) : (
              <KeyboardArrowLeft />
            )}
            Back
          </Button>
        }
      />
    </>
  );
};

export default CarouselCard;
