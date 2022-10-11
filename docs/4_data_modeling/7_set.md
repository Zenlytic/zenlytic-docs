---
sidebar_position: 7
---

# Sets

Sets are collections of [fields](9_field.md) that can be referenced throughout your data model. They're a convenient way to reference several fields over and over again instead of having to re-type the names.

Sets are always and only defined in [views](6_view.md). Although they can contain fields that are outside of the view they're defined in, there must be a path to join the views together to be able to reference fields in other views in a single set.

---

### Properties

Sets have only two properties:

`name`: (Required) The name of the set. If you reference this set elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)

`fields`: This is a list of fields that make up the set. There is a flexible syntax you can use to define the fields included in sets, which is discussed below.


### Field syntax

The syntax for specifying which fields to include in a list of fields is as follows.

You can include all available fields by using the special (case-sensitive) value `ALL_FIELDS*`.

You can include a single field by name by referencing its name. E.g. `customer_name` would include the field `customer_name`. If you want to include a field that is not in the base view, you'll need to specify the view name. For example, `customers.customer_name` would include that specific field, regardless of the view you are in.

You can un-include a single field by name by referencing its name with a negation before it. E.g. `-customer_name` would un-include the field `customer_name`. If you had two values specified, `[ALL_FIELDS*, -customer_name]` you would be including all available fields *except for* the `customer_name` field. As always, if you want to include a field that is not in the base view, you'll need to specify the view name. For example, `-customers.customer_name` would un-include that specific field, regardless of the view you are in.

You can include a set (even in the building of another set) by referencing its name and expanding it with the `*`. E.g. `my_set*` would include all fields defined in that set. If you are specifying fields in different views, you need to reference the view name for sets want to include or un-include. For example, `customers.my_set*` would include that all fields in that set.

You can un-include a set (even in the building of another set) by negating it, referencing its name and expanding it with the `*`. E.g. `-my_set*` would un-include all fields defined in that set. If you are specifying fields in different views, you need to reference the view name for sets want to include or un-include. For example, `-customers.my_set*` would un-include that all fields in that set.


These operations happen in order, so if you include a field early in your definition, then exclude it by excluding a set that the field is present in, the field will be excluded from the set. Vice versa, if you exclude the field early on in your definition, then later add it back in, it will be present in the set.

### Examples

Let's say we have a view with five (5) fields: `[customer_id, email, new_vs_repeat, state, city]`.

Let's define a set for the customer location. This only includes the `state` and `city` fields.
```
name: customer_location
fields: [state, city]
```

Let's define a set for the customer without PII. This will include all fields in the view except for `email`.
```
name: customer_no_pii
fields: [ALL_FIELDS*, -email]
```

Finally, let's define a set without PII and without location. We can use our existing building blocks for this one. In the first part of this definition we included the fields `customer_id`, `new_vs_repeat`, `state`, and `city`. Then we negated our set with `state` and `city`, which means our final set will only contain two fields `customer_id` and `new_vs_repeat`, which is exactly what we wanted.
```
name: customer_no_pii_no_location
fields: [customer_no_pii*, -customer_location]
```
