# How Zoë Ingests Context

Zoë, Zenlytic's AI data analyst, leverages multiple sources of context to understand your organization's data ecosystem, analytical philosophy, and business logic. This document explains the different ways Zoë learns about your data and how to optimize each source for better results.

## Context Sources

### 1. Custom System Prompt Context

You can extend Zoë's default system prompt with domain-specific knowledge that provides high-level organizational context:

- **Industry Context**: Specific business metrics, KPIs, and analytical patterns relevant to your sector
- **Company Terminology**: Internal terms, abbreviations, and naming conventions that differ from standard usage
- **Business Rules**: Unique calculation methods, data interpretation guidelines, or analytical frameworks your organization follows
- **Organizational Structure**: How departments, teams, or business units are organized and how this affects data analysis

**Optimization Tips:**
- Include glossaries of company-specific terms and their definitions
- Document any unique business rules or calculation methodologies that Zoë should always follow
- Explain organizational hierarchies and how they impact data interpretation and reporting
- Provide context about data quality considerations, known limitations, or special handling requirements

### 2. Fine-Tuning Examples

Zoë learns from examples of successfully answered questions to improve her performance:

- **Query Patterns**: Common ways users ask for similar data when she answers successfully
- **Field Usage**: How different measures and dimensions are typically combined for specific analyses
- **Response Preferences**: The analytical approaches and explanations that work best for your team

**Optimization Tips:**
- Review Zoë's responses and hit the thumbs up button to reinforce desired behavior
- Use the admin panel to remove any undesired or incorrectly marked examples
- Zoë will automatically prioritize frequently used fields in your workspace when making analytical decisions

### 3. YAML-Based Views

When using Zenlytic's native semantic layer, Zoë reads directly from your YAML view definitions to understand your data structure (see 4. for dbt Metricflow):

- **Field Definitions**: Views, measures, dimensions, and dimension groups, with field descriptions automatically imported from data warehouse metadata (Snowflake, BigQuery, Databricks, etc.)
- **Topic Structure**: How views join together through topics, including topic-level descriptions that provide analytical context
- **Access Controls**: User permissions that determine what data Zoë can access (she cannot see or reference data that users don't have permission to view)
- **Descriptions**: Both user-facing and AI-specific descriptions using the `description` and `zoe_description` attributes (Zoë uses `description` by default, but `zoe_description` takes precedence when both are defined)

**Optimization Tips:**
- Use the `zoe_description` attribute to provide AI-specific context that differs from user-facing descriptions
- Include business logic explanations in measure and dimension descriptions
- Document edge cases, calculation nuances, or limitations that Zoë should be aware of

### 4. dbt MetricFlow Integration (Optional)

When using dbt MetricFlow as your semantic layer (instead of Zenlytic's native ZenML), Zoë automatically ingests context from your dbt project:

- **Semantic Models**: Automatically mapped to Zenlytic views for seamless integration
- **Measures and Metrics**: Both dbt measures and metrics map to Zenlytic measures
- **Dimensions**: Converted to Zenlytic dimensions and dimension groups with appropriate time granularities
- **Relationships**: Join logic and entity relationships are preserved and automatically mapped to [topics](../data-modeling/topic.md)
- **Documentation**: Model and field descriptions carry over from dbt to provide business context for Zoë

**Optimization Tips:**
- Include rich, business-focused descriptions in your dbt models and fields
- Use clear, business-friendly naming conventions that will be intuitive for both, Zoë and your end users
- For advanced join logic beyond MetricFlow's capabilities, set `use_default_topics` to `false` in your `zenlytic_project.yml` file and define custom [topics](../data-modeling/topic.md) that reference your MetricFlow views

## Best Practices for Context Optimization

### Rich Descriptions
Always include business context in your field descriptions to help Zoë understand not just what the data is, but how it should be used:

```yaml
# Good: Provides business context
- name: customer_lifetime_value
  field_type: measure
  type: sum
  sql: ${TABLE}.clv
  description: Total revenue expected from a customer over their entire relationship
  zoe_description: Use this for retention analysis and customer segmentation. Calculated using predictive modeling on historical purchase patterns.

# Less helpful: Technical only
- name: customer_lifetime_value
  field_type: measure
  type: sum
  sql: ${TABLE}.clv
```

### Clear Topic Organization
Organize your topics with descriptive labels and rich context to help Zoë understand the analytical purpose:

```yaml
# Good: Descriptive topic with Zoë context
type: topic
label: Customer Analytics
base_view: customers
description: Customer data for retention and value analysis
zoe_description: Primary topic for customer health metrics, churn analysis, and segmentation. Includes predictive CLV calculations and behavioral scoring.
```

### Semantic Field Names
Use field names that clearly indicate their business purpose. While not essential since Zoë has extensive world knowledge, descriptive names benefit both, Zoë and your end users:
- `monthly_recurring_revenue` instead of `mrr`
- `customer_acquisition_cost` instead of `cac`
- `days_since_last_purchase` instead of `days_diff`

## Context Hierarchy

Zoë processes context sources in the following priority order:

1. **Custom system prompt context** - Company-specific rules, terminology, and high-level organizational knowledge
2. **Structural relationships** - How data connects through topics and joins, including topic-level descriptions
3. **Field and view descriptions** - Business context from YAML definitions or dbt documentation at the view, measure, and dimension level
4. **Fine-tuning examples** - Patterns from previous successful queries and responses that have been marked as helpful

Understanding this hierarchy helps you strategically place your most critical context in the highest-priority locations for maximum impact on Zoë's analytical performance.