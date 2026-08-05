import {
  AppBar,
  Toolbar,
  Typography,
  Avatar,
  Box,
} from "@mui/material";

export default function Header() {
  return (
    <AppBar position="static">
      <Toolbar>

        <Typography
          variant="h5"
          sx={{ flexGrow: 1 }}
        >
          NovaMed AI Control Tower
        </Typography>

        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            gap: 2,
          }}
        >
          <Typography>
            Ankit Gundewar
          </Typography>

          <Avatar>
            O
          </Avatar>
        </Box>

      </Toolbar>
    </AppBar>
  );
}