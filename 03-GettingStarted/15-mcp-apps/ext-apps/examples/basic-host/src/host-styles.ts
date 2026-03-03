/**
 * MCP style variables for the basic-host example.
 * These are passed to apps via hostContext.styles.variables.
 */
import type { McpUiStyles } from "@modelcontextprotocol/ext-apps";

/**
 * MCP App style variables using light-dark() for theme adaptation.
 * Apps receive these and can use them as CSS custom properties.
 */
export const HOST_STYLE_VARIABLES: McpUiStyles = {
  // Background colors - using light-dark() for automatic adaptation
  "--color-background-primary": "light-dark(#ffffff, #1a1a1a)",
  "--color-background-secondary": "light-dark(#f5f5f5, #2d2d2d)",
  "--color-background-tertiary": "light-dark(#e5e5e5, #404040)",
  "--color-background-inverse": "light-dark(#1a1a1a, #ffffff)",
  "--color-background-ghost": "light-dark(rgba(255,255,255,0), rgba(26,26,26,0))",
  "--color-background-info": "light-dark(#eff6ff, #1e3a5f)",
  "--color-background-danger": "light-dark(#fef2f2, #7f1d1d)",
  "--color-background-success": "light-dark(#f0fdf4, #14532d)",
  "--color-background-warning": "light-dark(#fefce8, #713f12)",
  "--color-background-disabled": "light-dark(rgba(255,255,255,0.5), rgba(26,26,26,0.5))",

  // Text colors
  "--color-text-primary": "light-dark(#1f2937, #f3f4f6)",
  "--color-text-secondary": "light-dark(#6b7280, #9ca3af)",
  "--color-text-tertiary": "light-dark(#9ca3af, #6b7280)",
  "--color-text-inverse": "light-dark(#f3f4f6, #1f2937)",
  "--color-text-ghost": "light-dark(rgba(107,114,128,0.5), rgba(156,163,175,0.5))",
  "--color-text-info": "light-dark(#1d4ed8, #60a5fa)",
  "--color-text-danger": "light-dark(#b91c1c, #f87171)",
  "--color-text-success": "light-dark(#15803d, #4ade80)",
  "--color-text-warning": "light-dark(#a16207, #fbbf24)",
  "--color-text-disabled": "light-dark(rgba(31,41,55,0.5), rgba(243,244,246,0.5))",

  // Border colors
  "--color-border-primary": "light-dark(#e5e7eb, #404040)",
  "--color-border-secondary": "light-dark(#d1d5db, #525252)",
  "--color-border-tertiary": "light-dark(#f3f4f6, #374151)",
  "--color-border-inverse": "light-dark(rgba(255,255,255,0.3), rgba(0,0,0,0.3))",
  "--color-border-ghost": "light-dark(rgba(229,231,235,0), rgba(64,64,64,0))",
  "--color-border-info": "light-dark(#93c5fd, #1e40af)",
  "--color-border-danger": "light-dark(#fca5a5, #991b1b)",
  "--color-border-success": "light-dark(#86efac, #166534)",
  "--color-border-warning": "light-dark(#fde047, #854d0e)",
  "--color-border-disabled": "light-dark(rgba(229,231,235,0.5), rgba(64,64,64,0.5))",

  // Ring colors (focus)
  "--color-ring-primary": "light-dark(#3b82f6, #60a5fa)",
  "--color-ring-secondary": "light-dark(#6b7280, #9ca3af)",
  "--color-ring-inverse": "light-dark(#ffffff, #1f2937)",
  "--color-ring-info": "light-dark(#2563eb, #3b82f6)",
  "--color-ring-danger": "light-dark(#dc2626, #ef4444)",
  "--color-ring-success": "light-dark(#16a34a, #22c55e)",
  "--color-ring-warning": "light-dark(#ca8a04, #eab308)",

  // Typography - Family
  "--font-sans": "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
  "--font-mono": "ui-monospace, 'SF Mono', Monaco, 'Cascadia Code', monospace",

  // Typography - Weight
  "--font-weight-normal": "400",
  "--font-weight-medium": "500",
  "--font-weight-semibold": "600",
  "--font-weight-bold": "700",

  // Typography - Text Size
  "--font-text-xs-size": "0.75rem",
  "--font-text-sm-size": "0.875rem",
  "--font-text-md-size": "1rem",
  "--font-text-lg-size": "1.125rem",

  // Typography - Heading Size
  "--font-heading-xs-size": "0.75rem",
  "--font-heading-sm-size": "0.875rem",
  "--font-heading-md-size": "1rem",
  "--font-heading-lg-size": "1.25rem",
  "--font-heading-xl-size": "1.5rem",
  "--font-heading-2xl-size": "1.875rem",
  "--font-heading-3xl-size": "2.25rem",

  // Typography - Text Line Height
  "--font-text-xs-line-height": "1.4",
  "--font-text-sm-line-height": "1.4",
  "--font-text-md-line-height": "1.5",
  "--font-text-lg-line-height": "1.5",

  // Typography - Heading Line Height
  "--font-heading-xs-line-height": "1.4",
  "--font-heading-sm-line-height": "1.4",
  "--font-heading-md-line-height": "1.4",
  "--font-heading-lg-line-height": "1.3",
  "--font-heading-xl-line-height": "1.25",
  "--font-heading-2xl-line-height": "1.2",
  "--font-heading-3xl-line-height": "1.1",

  // Border radius
  "--border-radius-xs": "2px",
  "--border-radius-sm": "4px",
  "--border-radius-md": "6px",
  "--border-radius-lg": "8px",
  "--border-radius-xl": "12px",
  "--border-radius-full": "9999px",

  // Border width
  "--border-width-regular": "1px",

  // Shadows
  "--shadow-hairline": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
  "--shadow-sm": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)",
  "--shadow-md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
  "--shadow-lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)",
};
