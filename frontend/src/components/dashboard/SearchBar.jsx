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
        label="Search Shipments"
        placeholder="Search by Shipment ID, Origin, Destination or Carrier"
        value={searchQuery}
        onChange={(event) => setSearchQuery(event.target.value)}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),

          endAdornment: searchQuery ? (
            <InputAdornment position="end">
              <IconButton
                onClick={handleClear}
                edge="end"
              >
                <ClearIcon />
              </IconButton>
            </InputAdornment>
          ) : null,
        }}
      />
    </Box>
  );
}