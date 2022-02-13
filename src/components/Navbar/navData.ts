export interface NavItem {
  label: string;
  subLabel?: string;
  children?: Array<NavItem>;
  href?: string;
}

export const NAV_ITEMS: Array<NavItem> = [
  {
    label: "Statistics",
    href: "/statistics",
  },
  {
    label: "Tags",
    href: "/tags",
  },
  {
    label: "PS",
    href: "/ps",
  },
  {
    label: "Dev",
    href: "/dev",
  },
  {
    label: "Note",
    href: "/note",
  },
];
