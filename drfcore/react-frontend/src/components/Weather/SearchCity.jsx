import { useState } from "react";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import clocks from "../common/data/clocks.json";
const SearchCity = ({ onCityChange }) => {
  const [selectedCity, setSelectedCity] = useState("Bangalore");
  const handleCityChange = (event, value) => {
    const trimmedValue = value.trim();
    const cityObject = clocks.find(
      (city) => city.name.toLowerCase() === trimmedValue.toLowerCase()
    );
    if (!cityObject) {
      const matchedCity = clocks.find((city) =>
        city.name.toLowerCase().startsWith(trimmedValue.toLowerCase())
      );
      if (matchedCity) {
        setSelectedCity(matchedCity.name);
        onCityChange(matchedCity);
      } else {
        alert("City not found. Please select a city from the list.");
      }
    } else {
      setSelectedCity(trimmedValue);
      onCityChange(cityObject);
    }
  };

  return (
    <Autocomplete
      freeSolo
      id="free-solo-2-demo"
      disableClearable
      options={clocks.map((option) => option.name)}
      onChange={handleCityChange}
      value={selectedCity}
      renderInput={(params) => (
        <TextField
          {...params}
          label="Search City"
          InputProps={{
            ...params.InputProps,
            type: "search",
          }}
        />
      )}
    />
  );
};

export default SearchCity;
