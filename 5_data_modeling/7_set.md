
# Sets

Sets are collections of [fields](9_field.md) that can be referenced throughout your data model. They're a convenient way to reference several fields over and over again instead of having to re-type the names.

Sets are always and only defined in [views](5_view.md). Although they can contain fields that are outside of the view they're defined in, there must be a path to join the views together to be able to reference fields in other views in a single set.

