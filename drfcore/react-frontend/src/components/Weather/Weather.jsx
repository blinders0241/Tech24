import clocks from "../common/data/clocks.json";
import { Paper, Grid, useTheme, Container } from "@mui/material";
import CarouselCard from "./CarouselCard";
import { useState } from "react";
import SearchCity from "./SearchCity";
import MainWeatherCard from "./MainWeatherCard";

const Weather = () => {
  const [selectedCity, setSelectedCity] = useState(clocks[2]);

  const handleCityChange = (city) => {
    setSelectedCity(city);
  };
  const handleCardCityChange = (city) => {
    setSelectedCity(city);
  };

  return (
    <>
      <Paper
        sx={{
          backgroundColor: "whitesmoke",
          borderRadius: "3px",
          justifyContent: "center",
          display: "flex",
          height: "100%",
          paddingTop: "2em",
          paddingBottom: "4em",
        }}
      >
        <Grid container maxWidth="lg">
          <Container>
            <SearchCity onCityChange={handleCityChange} />
          </Container>
          <Container sx={{ display: "flex" }}>
            <Container>
              <MainWeatherCard selectedCity={selectedCity} />
            </Container>
            <Container>
              <CarouselCard onCardCityChange={handleCardCityChange} />
            </Container>
          </Container>
        </Grid>
      </Paper>
    </>
  );
};
export default Weather;
