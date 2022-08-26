// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Zenlytic Docs',
  tagline: 'Modern self-serve analytics',
  url: 'https://docs.zenlytic.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'Zenlytic', // Usually your GitHub org/user name.
  projectName: 'zenlytic-docs', // Usually your repo name.
  trailingSlash: false,

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/Zenlytic/zenlytic-docs',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      algolia: {
        // The application ID provided by Algolia
        appId: '029VIRGT6M',
        // Public API key: it is safe to commit it
        apiKey: '1664be1f8d2107ebb3040175ea87987e',
        indexName: 'DOCS',
        searchPagePath: 'search',
      },
      navbar: {
        title: 'Zenlytic',
        logo: {
          alt: 'Zenlytic Logo',
          src: 'img/zenlytic-logo.jpeg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://github.com/Zenlytic/metrics_layer',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Documentation',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/zenlytic',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/pablankley',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Zenlytic/metrics_layer',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Ex Quanta, Inc.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
