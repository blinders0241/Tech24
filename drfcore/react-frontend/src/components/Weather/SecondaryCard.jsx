import React, { useEffect, useState } from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import { Alert, Container, Snackbar, useTheme } from "@mui/material";

const SecondaryCard = ({ partOfArray, onCityChange }) => {
  const theme = useTheme();
  const [dateState, setDateState] = useState(new Date());
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const handleSnackbarClose = () => {
    if (reason === "clickaway") {
      return;
    }
    setSnackbarOpen(false);
  };
  const handleCityChange = (item) => {
    const cityObject = partOfArray.find((city) => city.name === item.name);
    onCityChange(cityObject);
  };
  useEffect(() => {
    setInterval(() => setDateState(new Date()), 1000);
  }, []);
  return (
    <>
      {partOfArray.map((item) => (
        <Container>
          <Snackbar
            open={snackbarOpen}
            autoHideDuration={1000}
            onClose={handleSnackbarClose}
          >
            <Alert
              onClose={handleSnackbarClose}
              severity="success"
              sx={{ width: "100%" }}
            >
              Time copied to clipboard
            </Alert>
          </Snackbar>
          <Card
            sx={{
              height: 200,
              width: 200,
              mt: "7em",
              ml: "-10px",
              mb: "3em",
              borderRadius: "6px",
            }}
          >
            <CardContent>
              <Typography
                gutterBottom
                variant="h5"
                component="div"
                sx={{ textAlign: "center", padding: "10px" }}
                onClick={() => handleCityChange(item)}
              >
                {item.name}
              </Typography>
              <Typography
                color={theme.palette.warning.main}
                align="center"
                variant="body2"
                sx={{ padding: "5px" }}
              >
                GMT {item.timediff}{" "}
              </Typography>
              <Typography
                align="center"
                variant="h5"
                sx={{ padding: "15px" }}
                onClick={() => {
                  navigator.clipboard.writeText(
                    dateState.toLocaleTimeString("en-US", {
                      hour: "numeric",
                      minute: "numeric",
                      second: "numeric",
                      hour12: false,
                      timeZone: item.timeZone,
                    })
                  );
                  setSnackbarOpen(true);
                }}
              >
                {dateState.toLocaleTimeString("en-US", {
                  hour: "numeric",
                  minute: "numeric",
                  second: "numeric",
                  hour12: true,
                  timeZone: item.timeZone,
                })}
              </Typography>
            </CardContent>
          </Card>
        </Container>
      ))}
    </>
  );
};

export default SecondaryCard;
