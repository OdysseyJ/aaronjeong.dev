import {
  Box,
  BoxProps,
  Link,
  Stack,
  useColorModeValue,
} from "@chakra-ui/react";
import { NAV_ITEMS } from "@src/components/Navbar/navData";
import NextLink from "next/link";
import {useRouter} from "next/router";

export const DesktopNav = (props: BoxProps) => {
  const router = useRouter()

  return (
    <Stack direction={"row"} spacing={4} {...props}>
      {NAV_ITEMS.map((navItem) => (
        <Box key={navItem.label} borderRadius={10} padding={2} bg={router.asPath.includes(navItem.href || "") ? useColorModeValue("gray.200", "white") : ""}>
          <NextLink href={navItem.href ?? "#"} passHref >
            <Link
              p={2}
              fontSize={"sm"}
              fontWeight={500}
              outline={"none"}
              color={router.asPath.includes(navItem.href || "") ? useColorModeValue("gray.600", "black") : useColorModeValue("gray.600", "gray.200")}
              _hover={{
                textDecoration: "none",
                fontWeight: 800,
              }}
            >
              {navItem.label}
            </Link>
          </NextLink>
        </Box>
      ))}
    </Stack>
  );
};
