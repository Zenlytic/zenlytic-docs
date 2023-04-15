import React from "react";
import { MendableSearchBar } from "@mendable/search";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";

export default function SearchBarWrapper() {
  const {
    siteConfig: { customFields },
  } = useDocusaurusContext();
  return (
    <div className="mendable-search">
      <MendableSearchBar
        anon_key={customFields.mendableAnonKey}
        style={{ accentColor: "#ECFFA1", darkMode: true }}
        placeholder="Search..."
        dialogPlaceholder="How to I create a view?"
      />
    </div>
  );
}
