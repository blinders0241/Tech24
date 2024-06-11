import { useEffect, useState } from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { Grid, useTheme } from "@mui/material";
import WindIcon from "@mui/icons-material/Cloud";
import HumidityIcon from "@mui/icons-material/Opacity";
import Clear from "../../assets/images/Clear.jpg";
import Fog from "../../assets/images/fog.png";
import Cloudy from "../../assets/images/Cloudy.jpg";
import Rainy from "../../assets/images/Rainy.jpg";
import Snow from "../../assets/images/snow.jpg";
import Stormy from "../../assets/images/Stormy.jpg";
import Smoke from "../../assets/images/Smoke.jpg";
import Sunny from "../../assets/images/Sunny.jpg";
import Overcast from "../../assets/images/Overcast.jpg";
const images = {
  Clear,
  Fog,
  Cloudy,
  Rainy,
  Snow,
  Stormy,
  Sunny,
  Smoke,
  Overcast,
};
const MainWeatherCard = ({ selectedCity }) => {
  const [weatherCondition, setWeatherCondition] = useState("");
  const [weatherIcon, setWeatherIcon] = useState("");
  const [data, setData] = useState("");
  const [iconLink, setIconLink] = useState("");
  const [humidity, setHumidity] = useState("");
  const [feelsLike, setFeelsLike] = useState("");
  const [windSpeed, setWindSpeed] = useState("");
  const theme = useTheme();
  const [dateState, setDateState] = useState(new Date());
  const [allWeatherInfo, setAllWeatherInfo] = useState("");
  const [image, setImage] = useState(images.Clear);

  const getWeather = async () => {
    const res = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${selectedCity.name}&appid=5d59d6d155f59e8c1963a082125a039a&units=metric`
    );
    const resData = await res.json();
    setWeatherCondition(resData.weather[0].description);
    setWeatherIcon(resData.weather[0].icon);
    setData(resData.main.temp);
    setHumidity(resData.main.humidity);
    setFeelsLike(resData.main.feels_like);
    setWindSpeed(resData.wind.speed);
    setIconLink(
      "https://openweathermap.org/img/wn/" + resData.weather[0].icon + "@2x.png"
    );
    setAllWeatherInfo(resData.weather[0].main);
  };
  useEffect(() => {
    if (allWeatherInfo) {
      const conditions = allWeatherInfo;
      switch (conditions.toLowerCase()) {
        case "clear":
          setImage(images.Clear);
          break;
        case "clouds":
          setImage(images.Cloudy);
          break;
        case "overcast clouds":
          setImage(images.Overcast);
          break;
        case "rain":
          setImage(images.Rainy);
          break;
        case "snow":
          setImage(images.Snow);
          break;
        case "mist":
          setImage(images.Fog);
          break;
        case "fog":
          setImage(images.Fog);
          break;
        case "smoke":
          setImage(images.Smoke);
          break;
        case "thunderstorm":
          setImage(images.Stormy);
          break;
        default:
          setImage(images.Sunny);
          break;
      }
    }
  }, [allWeatherInfo]);
  useEffect(() => {
    getWeather();
  }, [selectedCity]);
  useEffect(() => {
    setInterval(() => setDateState(new Date()), 1000);
  }, []);
  return (
    <Card
      sx={{
        height: 400,
        width: 345,
        mt: "2em",
        ml: "-5px",
        mb: "2em",
        position: "relative",
        background: "none",
      }}
    >
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          backgroundImage: `url(${image})`,
          backgroundSize: "cover",
          backgroundRepeat: "no-repeat",
          opacity: 0.3,
          borderRadius: "6px",
        }}
      />
      <CardContent sx={{ fontWeight: theme.typography.fontWeightBold }}>
        <Typography
          gutterBottom
          variant="h5"
          component="div"
          sx={{ textAlign: "center", pt: "10px" }}
        >
          {selectedCity.name}
        </Typography>
        <CardMedia
          component="img"
          sx={{ height: 120, objectFit: "contain" }}
          image={iconLink}
          alt={selectedCity.name}
        />
        <Typography
          gutterBottom
          variant="h5"
          component="div"
          sx={{ textAlign: "center" }}
        >
          {data}°C
        </Typography>
        <Typography
          gutterBottom
          sx={{ textAlign: "center", mt: "-7px", mb: "10px" }}
        >
          {weatherCondition}
        </Typography>
        <Grid container alignItems="center" justifyContent="center" spacing={2}>
          <Grid
            item
            xs={6}
            sx={{ display: "flex", alignItems: "center", ml: "-25px" }}
          >
            <HumidityIcon />
            <Grid
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
              }}
            >
              <Typography gutterBottom>{humidity}%</Typography>
              <Typography gutterBottom sx={{ mt: "-10px", pl: "7px" }}>
                Humidity
              </Typography>
            </Grid>
          </Grid>
          <Grid
            item
            xs={6}
            sx={{ display: "flex", alignItems: "center", mr: "-75px" }}
          >
            <WindIcon />
            <Grid
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
              }}
            >
              <Typography gutterBottom>{windSpeed}m/s</Typography>
              <Typography gutterBottom sx={{ mt: "-10px", pl: "7px" }}>
                Wind Speed
              </Typography>
            </Grid>
          </Grid>
        </Grid>
        <Typography gutterBottom sx={{ textAlign: "center" }}>
          Feels like {feelsLike}°C
        </Typography>
        <Grid container alignItems="center" justifyContent="center" spacing={2}>
          <Grid item xs={6} sx={{ display: "flex", alignItems: "center" }}>
            <Grid
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                ml: "-25px",
              }}
            >
              <Typography
                gutterBottom
                align="center"
                variant="h5"
                sx={{ padding: "10px" }}
              >
                {dateState.toLocaleTimeString("en-US", {
                  hour: "numeric",
                  minute: "numeric",
                  second: "numeric",
                  hour12: true,
                  timeZone: selectedCity.timeZone,
                })}
              </Typography>
            </Grid>
          </Grid>
          <Grid
            item
            xs={6}
            sx={{
              display: "flex",
              alignItems: "center",
              mt: "-10px",
              mr: "-75px",
            }}
          >
            <Grid
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
              }}
            >
              <Typography color={theme.palette.warning.main} align="center">
                GMT {selectedCity.timediff}{" "}
              </Typography>
            </Grid>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};

export default MainWeatherCard;
