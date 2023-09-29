import React from "react";
import { MendableSearchBar } from "@mendable/search";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useThemeContext from '@theme/hooks/useThemeContext';
import BrowserOnly from '@docusaurus/BrowserOnly';


export default function SearchBarWrapper() {
  const {
    siteConfig: { customFields },
  } = useDocusaurusContext();
  const { isDarkTheme } = useThemeContext();
  return (
    <div className="mendable-search">
        <BrowserOnly>
            {() => {
            return <MendableSearchBar
                anon_key={customFields.mendableAnonKey}
                style={{ accentColor: "#ECFFA1", darkMode: isDarkTheme, ariaLabel: 'Search' }}
                placeholder="Search..."
                dialogPlaceholder="How to I create a view?"
                showSimpleSearch={true}
                />;
            }}
        </BrowserOnly>
    </div>
  );
}
