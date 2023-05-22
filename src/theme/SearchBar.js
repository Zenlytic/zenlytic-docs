import React from "react";
import { MendableSearchBar } from "@mendable/search";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import BrowserOnly from '@docusaurus/BrowserOnly';


export default function SearchBarWrapper() {
  const {
    siteConfig: { customFields },
  } = useDocusaurusContext();
  return (
    <div className="mendable-search">
        <BrowserOnly>
            {() => {
            return <MendableSearchBar
                anon_key={customFields.mendableAnonKey}
                style={{ accentColor: "#ECFFA1", darkMode: true, ariaLabel: 'Search' }}
                placeholder="Search..."
                dialogPlaceholder="How to I create a view?"
                showSimpleSearch={true}
                />;
            }}
        </BrowserOnly>
    </div>
  );
}
