import {
  Box,
  IconButton,
  InputAdornment,
  TextField,
} from "@mui/material";

import ClearIcon from "@mui/icons-material/Clear";
import SearchIcon from "@mui/icons-material/Search";

import { useShipmentContext } from "../../context/useShipmentContext";

export default function SearchBar() {
  const {
    searchQuery,
    setSearchQuery,
  } = useShipmentContext();

  function handleClear() {
    setSearchQuery("");
  }

  return (
    <Box>
      <TextField
        fullWidth
        variant="outlined"
        placeholder="Search by Shipment ID, Origin, Destination or Carrier"
        value={searchQuery}
        onChange={(event) => setSearchQuery(event.target.value)}
        slotProps={{
          input: {
            startAdornment: (
              <InputAdornment
                position="start"
                sx={{
                  mr: 1,
                }}
              >
                <SearchIcon
                  sx={{
                    color: "primary.main",
                    fontSize: 22,
                  }}
                />
              </InputAdornment>
            ),

            endAdornment: searchQuery ? (
              <InputAdornment
                position="end"
                sx={{
                  ml: 1,
                }}
              >
                <IconButton
                  edge="end"
                  onClick={handleClear}
                  size="small"
                >
                  <ClearIcon
                    sx={{
                      color: "primary.main",
                      fontSize: 22,
                    }}
                  />
                </IconButton>
              </InputAdornment>
            ) : null,
          },
        }}
        sx={{
          "& .MuiInputBase-input": {
            py: 1.6,
          },
        }}
      />
    </Box>
  );
}