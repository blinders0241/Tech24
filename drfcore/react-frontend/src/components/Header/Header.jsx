import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import { Link } from "react-router-dom";
import ThemeSwitch from "../customs/styled/ThemeSwitch";
import { useTheme } from "@emotion/react";
import { useContext } from "react";
import { ColorModeContext } from "../../theme/CustomThemeProvider";
import Clock from "./Clock";
import logo from "../../../assets/logo3.png";
import { Typography } from "@mui/material";
import { TiWeatherPartlySunny } from "react-icons/ti";

// import React from "react";
function BasicExample() {
  const theme = useTheme();
  const colorMode = useContext(ColorModeContext);
  return (
    <Navbar expand="lg" className="bg-body-tertiary justify-content-between">
      <Container>
        <img src={logo} width="50" height="50" />
        <Typography
          variant="h6"
          component={Link}
          to="/"
          sx={{
            color: theme.palette.primary.contrastText,
            textDecoration: "none",
            letterSpacing: "2px",
            marginLeft: "12px",
            marginRight: "24px",
            fontStyle: "oblique",
            fontWeight: "bold",
            fontSize: "38px", // text size
            "&:hover": {
              color: theme.palette.secondary.main,
            },
          }}
        >
          FarFlix
        </Typography>

        <Navbar.Brand>
          <Link to="/" style={{ textDecoration: "none" }}>
            Notes
          </Link>{" "}
          &nbsp; |&nbsp;
          <Link to="/displayStockdetails" style={{ textDecoration: "none" }}>
            Finance
          </Link>
          &nbsp; |&nbsp;
          <Link to="/FarFlixSearch" style={{ textDecoration: "none" }}>
            Movies
          </Link>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <NavDropdown title="Notes" id="basic-nav-dropdown">
              <NavDropdown.Item>
                <Link to="/notes" style={{ textDecoration: "none" }}>
                  Add Note
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item>
                <Link to="/markdown" style={{ textDecoration: "none" }}>
                  MarkDown
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item>
            </NavDropdown>

            <NavDropdown title="Finance" id="basic-nav-dropdown">
              <NavDropdown.Item>
                <Link
                  to="/displayStockdetails"
                  style={{ textDecoration: "none" }}
                >
                  Stock Futures
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item>
                <Link
                  to="/displayIndexdetails"
                  style={{ textDecoration: "none" }}
                >
                  Index Futures
                </Link>
              </NavDropdown.Item>

              <NavDropdown.Item>
                {" "}
                <Link
                  to="/displayEquityetails"
                  style={{ textDecoration: "none" }}
                >
                  Equities
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item>
                <Link to="/uploadData" style={{ textDecoration: "none" }}>
                  Upload BhavCopy
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item>
                <Link to="/uploadequity" style={{ textDecoration: "none" }}>
                  Upload Equity
                </Link>
              </NavDropdown.Item>
            </NavDropdown>

            <NavDropdown title="Movies" id="basic-nav-dropdown">
              <NavDropdown.Item>
                <Link to="/FarFlixhome" style={{ textDecoration: "none" }}>
                  Movies Home
                </Link>
              </NavDropdown.Item>

              <NavDropdown.Item>
                <Link to="/FarFlixSearch" style={{ textDecoration: "none" }}>
                  Search Movies
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item>
                <Link to="/FarFlixUpload" style={{ textDecoration: "none" }}>
                  Movies Upload
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item>
                <Link
                  to="/FFMovieDetailsUpload"
                  style={{ textDecoration: "none" }}
                >
                  FF Movies Details Upload
                </Link>
              </NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>

        <Link to="/Weather" style={{ textDecoration: "none" }}>
          <h3>
            <TiWeatherPartlySunny />
          </h3>
        </Link>
        {/* Clock PLACING */}
        <Clock />

        <ThemeSwitch
          checked={theme.palette.type === "dark"}
          onClick={colorMode.toggleColorMode}
        />
      </Container>
    </Navbar>
  );
}

export default BasicExample;
