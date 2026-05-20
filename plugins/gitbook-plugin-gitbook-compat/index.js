function renderMarkdown(block) {
  return this.renderBlock("markdown", block.body);
}

module.exports = {
  blocks: {
    code: {
      process: renderMarkdown,
    },
    stepper: {
      process: renderMarkdown,
    },
    step: {
      process: renderMarkdown,
    },
  },
};
